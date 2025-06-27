from nicegui.testing import User
from nicegui import ui
import pytest


async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    
    # Check initial counter display
    await user.should_see('0')


async def test_counter_increment(user: User) -> None:
    """Test incrementing the counter"""
    await user.open('/')
    
    # Find increment button and click it
    user.find(marker='increment_btn').click()
    
    # Check counter was incremented
    await user.should_see('1')


async def test_counter_decrement(user: User) -> None:
    """Test decrementing the counter"""
    await user.open('/')
    
    # First increment to have a positive number
    user.find(marker='increment_btn').click()
    
    # Then decrement
    user.find(marker='decrement_btn').click()
    
    # Check counter is back to 0
    await user.should_see('0')


async def test_counter_negative_values(user: User) -> None:
    """Test that counter can go negative"""
    await user.open('/')
    
    # Click decrement button
    user.find(marker='decrement_btn').click()
    
    # Check counter is -1
    await user.should_see('-1')


async def test_counter_reset(user: User) -> None:
    """Test resetting the counter"""    
    await user.open('/')
    
    # Increment counter multiple times
    for _ in range(5):
        user.find(marker='increment_btn').click()
    
    # Click reset button
    user.find(marker='reset_btn').click()
    
    # Check counter is back to 0
    await user.should_see('0')


async def test_counter_persistence(user: User) -> None:
    """Test that counter value persists in user storage"""
    await user.open('/')
    
    # Increment counter three times
    for _ in range(3):
        user.find(marker='increment_btn').click()
    
    # Check we can see the value 3
    await user.should_see('3')
    
    # Simulate page reload by opening the page again
    await user.open('/')
    
    # Counter should still show the same value due to user storage
    await user.should_see('3')


async def test_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Perform a series of operations: +3, -1, +2, -5
    for _ in range(3):
        user.find(marker='increment_btn').click()
    
    user.find(marker='decrement_btn').click()
    
    for _ in range(2):
        user.find(marker='increment_btn').click()
    
    for _ in range(5):
        user.find(marker='decrement_btn').click()
    
    # Final result should be 3 - 1 + 2 - 5 = -1
    await user.should_see('-1')


async def test_ui_elements_present(user: User) -> None:
    """Test that all UI elements are present"""
    await user.open('/')
    
    # Check for title
    await user.should_see('Counter Application')
    
    # Check for buttons by their markers
    await user.should_see(marker='increment_btn')
    await user.should_see(marker='decrement_btn')
    await user.should_see(marker='reset_btn')
    
    # Check initial counter value
    await user.should_see('0')


async def test_button_functionality_sequence(user: User) -> None:
    """Test a complex sequence of button operations"""
    await user.open('/')
    
    # Start with increment
    user.find(marker='increment_btn').click()
    await user.should_see('1')
    
    user.find(marker='increment_btn').click()
    await user.should_see('2')
    
    # Decrement once
    user.find(marker='decrement_btn').click()
    await user.should_see('1')
    
    # Reset
    user.find(marker='reset_btn').click()
    await user.should_see('0')
    
    # Go negative
    user.find(marker='decrement_btn').click()
    await user.should_see('-1')
    
    user.find(marker='decrement_btn').click()
    await user.should_see('-2')
    
    # Back to positive
    user.find(marker='increment_btn').click()
    await user.should_see('-1')
    
    user.find(marker='increment_btn').click()
    await user.should_see('0')
    
    user.find(marker='increment_btn').click()
    await user.should_see('1')