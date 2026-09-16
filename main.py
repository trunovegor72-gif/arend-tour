from datetime import date

equipment = "Палатка 123"
category = "Палатки"
price_per_day = 450.0
total_count = 5
available_count = 3

client = "Иванов Иван Иванович"
quantity = 2
start_date = date(2026, 9, 12)
end_date = date(2026, 9, 21)
return_date = date(2026, 9, 23)


def check_availability(available, requested):
    if available == 0:
        return "Нет в наличии"
    if available < requested:
        return "Доступно только " + str(available) + " шт."
    return "Доступно " + str(available) + " шт."


def calculate_cost(price, count, days):
    cost = price * count * days
    return round(cost, 2)


def calculate_penalty(price, count, end, returned):
    overdue = (returned - end).days
    if overdue > 0:
        return round(price * count * overdue * 1.5, 2)
    return 0


def get_status(end, returned):
    if returned > end:
        return "просрочена"
    return "завершена"


days = (end_date - start_date).days
cost = calculate_cost(price_per_day, quantity, days)
deposit = int(cost * 0.3)
penalty = calculate_penalty(price_per_day, quantity, end_date, return_date)
status = get_status(end_date, return_date)

print("Оборудование:", equipment, "(" + category + ")")
print("Тариф:", price_per_day, "руб. в сутки")
print(check_availability(available_count, quantity))
print()
print("Клиент:", client)
print("Аренда с", start_date, "по", end_date, "-", days, "суток")
print("Количество:", quantity, "шт.")
print("Стоимость аренды:", cost, "руб.")
print("Залог:", deposit, "руб.")
print()
print("Дата возврата:", return_date)
print("Штраф за просрочку:", penalty, "руб.")
print("Итого к оплате:", cost + penalty, "руб.")
print("Статус аренды:", status)
