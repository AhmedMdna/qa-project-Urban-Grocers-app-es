import sender_stand_request
import data

def positive_assert(name):
    kit_name = sender_stand_request.post_new_client_kit(name)

    # Comprueba si el código de estado es 201
    assert kit_name.status_code == 201
    # Comprueba que el campo name probado es igual al de la respuesta
    assert kit_name.json()["name"] == name

def negative_assert_code_400(name):
    kit_name = sender_stand_request.post_new_client_kit(name)

    # Comprueba si el código de estado es 400
    assert kit_name.status_code == 400

def test_1_create_kit_name_1_letter():
    positive_assert(data.one_letter)

def test_2_create_kit_name_511_letters():
    positive_assert(data.long_name_511)

def test_3_create_kit_name_0_letters():
    negative_assert_code_400(data.empty_string)

def test_4_create_kit_name_512_letters():
    negative_assert_code_400(data.long_name_512)

def test_5_create_kit_name_special_char_allowed():
    positive_assert(data.special_chars)

def test_6_create_kit_name_spaces_allowed():
    positive_assert(data.with_spaces)

def test_7_create_kit_name_numbers_allowed():
    positive_assert(data.numbers)

def test_8_create_kit_name_empty():
    negative_assert_code_400(None)

def test_9_create_kit_name_diff_type():
    negative_assert_code_400(data.number_type)