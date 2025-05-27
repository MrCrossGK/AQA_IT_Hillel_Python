import pytest
from func_for_tst import is_palindrome, status_info

@pytest.mark.parametrize(
  "in_data,res",
  [
    ("kalak asa kalak", True),
    ("kalak as kalak", False),
    ("pull up if I pull up", True)
  ])
def test_func(in_data, res):
  act_res = is_palindrome(in_data)
  exp_res = res
  assert act_res == exp_res


tickets = [
    {"ticket_id": 1, "price": 100, "status": "sold"},
    {"ticket_id": 2, "price": 200, "status": "available"},
    {"ticket_id": 4, "price": 200, "status": None},
    {"ticket_id": 3, "price": 150, "status": "sold"},
    {"ticket_id": 4, "status": None},
    {"ticket_id": 5, "price": 250, "status": "available"},
    {"ticket_id": 6, "price": 0, "status": "available"},
    {"ticket_id": 7, "status": "available"}
]
s_100_tickets = [{"ticket_id": 1, "price": 100, "status": "sold"}]
a_250_tickets = [{"ticket_id": 5, "price": 250, "status": "available"}]


@pytest.mark.parametrize(
    "in_data,price,status,res",
    [
        (tickets, 100, "sold", s_100_tickets),
        (tickets, 250, "available", a_250_tickets),
    ])
def test_stat_info(in_data, price, status, res):
    act_res = status_info(in_data, price, status)
    exp_res = res
    assert act_res == exp_res
