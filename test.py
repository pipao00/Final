import stand_request


# Богданов Андрей, 10-я когорта — Финальный проект. Инженер по тестированию плюс
# Тест для проверки создания заказа
def test_order_creation():
    order_response = stand_request.post_new_order()
    track_id = order_response.json()['track']
    response = stand_request.get_track(track_id)
    assert response.status_code == 200