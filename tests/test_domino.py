import pytest
from fortytwo.domino import Domino


@pytest.fixture
def sample_dominoes():
    return {
        "domino1": Domino(3, 4),
        "domino2": Domino(5, 5),
        "domino3": Domino(2, 3),
        "domino4": Domino(4, 6)
    }


# Direct creation test - ensures the class can be initialized properly
@pytest.mark.parametrize("side_one, side_two, exp_natural_suit", [
    (1, 2, 2),     # side_two is larger
    (5, 3, 5),     # side_one is larger
    (4, 4, 4),     # both sides equal
    (0, 6, 6),     # zero on one side
])
def test_domino_creation(side_one, side_two, exp_natural_suit):
    """Test creating dominoes with different values"""
    domino = Domino(side_one, side_two)
    assert domino.sideOne == side_one
    assert domino.sideTwo == side_two
    assert domino.natural_suit == exp_natural_suit


# Tests for value constraints that should be enforced
@pytest.mark.parametrize("side_one, side_two, should_raise, error_message", [
    (0, 0, False, None),      # Valid - Both sides zero
    (6, 6, False, None),      # Valid - Maximum allowed value
    (3, 4, False, None),      # Valid - Normal values
    (7, 5, True, "Domino values must be between 0 and 6"),       # Invalid - First value too high
    (5, 7, True, "Domino values must be between 0 and 6"),       # Invalid - Second value too high
    (-1, 5, True, "Domino values must be between 0 and 6"),      # Invalid - Negative number
    (3.5, 4, True, "Domino values must be integers"),     # Invalid - Float value
    ("3", 4, True, "Domino values must be integers"),     # Invalid - String value
    (None, 4, True, "Domino values must be integers"),    # Invalid - None value
])
def test_value_constraints(side_one, side_two, should_raise, error_message):
    """Test that the Domino class enforces valid domino values (0-6 integers)"""
    if should_raise:
        with pytest.raises((ValueError, TypeError)) as excinfo:
            Domino(side_one, side_two)
        # Check that error message matches expectation
        assert str(excinfo.value) == error_message
    else:
        # Should not raise an exception
        domino = Domino(side_one, side_two)
        assert domino.sideOne == side_one
        assert domino.sideTwo == side_two
        # The natural suit should always be valid
        assert 0 <= domino.natural_suit <= 6


def test_initialization(sample_dominoes):
    """Test the initialization and properties of Domino"""
    domino1 = sample_dominoes["domino1"]
    domino2 = sample_dominoes["domino2"]
    
    assert domino1.sideOne == 3
    assert domino1.sideTwo == 4
    assert domino1.natural_suit == 4

    assert domino2.sideOne == 5
    assert domino2.sideTwo == 5
    assert domino2.natural_suit == 5


@pytest.mark.parametrize("domino_key, expected", [
    ("domino1", False),  # 3,4 - not a double
    ("domino2", True),   # 5,5 - a double
    ("domino3", False),  # 2,3 - not a double
    ("domino4", False),  # 4,6 - not a double
])
def test_is_double(sample_dominoes, domino_key, expected):
    """Test the is_double method using parametrization"""
    assert sample_dominoes[domino_key].is_double() == expected


@pytest.mark.parametrize("domino_key, lead_suit, expected, scenario", [
    ("domino1", None, 4, "No lead suit - return natural suit"),
    ("domino1", 3, 3, "Lead suit matching sideOne"),
    ("domino1", 4, 4, "Lead suit matching sideTwo"),
    ("domino1", 6, 4, "Lead suit matching neither side - return natural suit"),
    ("domino2", 5, 5, "Double domino - lead suit matching both sides"),
])
def test_get_suit(sample_dominoes, domino_key, lead_suit, expected, scenario):
    """Test the get_suit method with various lead suits using parametrization"""
    assert sample_dominoes[domino_key].get_suit(lead_suit) == expected


@pytest.mark.parametrize("domino_key, expected, comment", [
    ("domino1", False, "3+4=7, not divisible by 5"),
    ("domino2", True, "5+5=10, divisible by 5"),
    ("domino3", True, "2+3=5, divisible by 5"),
    ("domino4", True, "4+6=10, divisible by 5"),
])
def test_is_count(sample_dominoes, domino_key, expected, comment):
    """Test the is_count method using parametrization"""
    assert sample_dominoes[domino_key].is_count() == expected


@pytest.mark.parametrize("domino_key, expected, comment", [
    ("domino1", 0, "3+4=7, not divisible by 5, returns 0"),
    ("domino2", 10, "5+5=10, divisible by 5, returns 10"),
    ("domino3", 5, "2+3=5, divisible by 5, returns 5"),
    ("domino4", 10, "4+6=10, divisible by 5, returns 10"),
])
def test_get_value(sample_dominoes, domino_key, expected, comment):
    """Test the get_value method using parametrization"""
    assert sample_dominoes[domino_key].get_value() == expected


@pytest.mark.parametrize("domino_key, expected", [
    ("domino1", "Domino(3, 4)"),
    ("domino2", "Domino(5, 5)"),
])
def test_repr(sample_dominoes, domino_key, expected):
    """Test the __repr__ method using parametrization"""
    assert repr(sample_dominoes[domino_key]) == expected


@pytest.mark.parametrize("domino_key, expected_output", [
    ("domino1", "+---+\n| 3 |\n|---|\n| 4 |\n+---+"),
    ("domino2", "+---+\n| 5 |\n|---|\n| 5 |\n+---+"),
])
def test_str(sample_dominoes, domino_key, expected_output):
    """Test the __str__ method using parametrization"""
    assert str(sample_dominoes[domino_key]) == expected_output