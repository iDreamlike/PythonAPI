import requests


class TestFirstAPI:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Sergey'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Неверный код ответа"

        response_dict = response.json()
        assert "answer" in response_dict, "Нет поля 'answer' в ответе"

        expected_response_test = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_test, "Актуальный текст "