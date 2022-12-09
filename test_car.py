import pytest as pytest
from unittest.mock import patch


def test_is_engine_started_return_true():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=10,
              tyre_friction=5)
    # Act
    car.start_engine()
    # Assert
    assert car.is_engine_started is True


def test_is_accelerated_increase_sped():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=10,
              tyre_friction=5)
    # Act
    car.start_engine()
    car.accelerate()
    # Assert
    assert car.current_speed == 10


def test_accelerate_for_max_limit_increases_till_max_speed():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=20, acceleration=10,
              tyre_friction=5)
    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    # Assert
    assert car.current_speed == 20


def test_apply_break_for_car_decreases_speed():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=10,
              tyre_friction=5)
    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.apply_break()
    # Assert
    assert car.current_speed == 15


def test_apply_break_min_limit_not_less_then_zero():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=5,
              tyre_friction=7)
    # Act
    car.start_engine()
    car.accelerate()
    car.apply_break()
    # Assert
    assert car.current_speed == 0


@patch('builtins.print')
def test_sound_horn_when_engine_is_on(mock_print):
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=5,
              tyre_friction=7)
    # Act
    car.start_engine()
    car.sound_horn()
    # Assert
    mock_print.assert_called_with("Beep Beep")


@patch('builtins.print')
def test_sound_horn_when_engine_is_of(mock_print):
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=5,
              tyre_friction=7)
    # Act
    car.sound_horn()
    # Assert
    mock_print.assert_called_with("Start the engine to sound_horn")


def test_stop_engine_return_false():
    # Arrange
    from car import Car
    car = Car(color="Narangi", max_speed=100, acceleration=5,
              tyre_friction=7)
    # Act
    car.start_engine()
    car.stop_engine()
    # Assert
    assert car.is_engine_started is False


def test_exception_for_max_speed_not_less_then_zero():
    from car import Car
    with pytest.raises(ValueError) as e:
        assert Car(color="Narangi", max_speed=-6, acceleration=5,
                   tyre_friction=7)
    assert str(e.value) == 'Invalid value for max_speed'


def test_exception_for_acceleration_not_less_then_zero():
    from car import Car
    with pytest.raises(ValueError) as e:
        assert Car(color="Narangi", max_speed=6, acceleration=-3,
                   tyre_friction=7)
    assert str(e.value) == 'Invalid value for acceleration'


def test_exception_for_tyre_friction_not_less_then_zero():
    from car import Car
    with pytest.raises(ValueError) as e:
        assert Car(color="Narangi", max_speed=6, acceleration=3,
                   tyre_friction=-7)
    assert str(e.value) == 'Invalid value for tyre_friction'
