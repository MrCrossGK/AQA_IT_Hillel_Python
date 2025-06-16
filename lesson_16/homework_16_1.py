import pytest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        Employee.__init__(self, name, salary)


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)


def get_attr(obj, attr_name, default, exp_type):
    if hasattr(obj, attr_name):
        value = getattr(obj, attr_name)
        if exp_type is not None and not isinstance(value, exp_type):
            raise TypeError(f"Атрибут '{attr_name}' найден, но не является типом {exp_type.__name__}")
        return value
    return default


@pytest.fixture
def team_lead():
    return TeamLead("Tom", 4000, "Panel_team", "Python", 13)


def test_depart_req_attr():
    tl = TeamLead("Tom", 4000, "Panel_team", "Python", 13)
    assert hasattr(tl, "department"), "There is No \"department\" attribute!"


def test_prog_lang_req_attr():
    tl = TeamLead("Tom", 4000, "Panel_team", "Python", 13)
    assert hasattr(tl, "programming_language"), "There is No \"programming_language\" attribute!"


def test_team_size_req_attr():
    tl = TeamLead("Tom", 4000, "Panel_team", "Python", 13)
    assert hasattr(tl, "team_size"), "There is No \"team_size\" attribute!"


def test_name_req_attr():
    tl = TeamLead("Tom", 4000, "Panel_team", "Python", 13)
    assert hasattr(tl, "name"), "There is No \"name\" attribute!"


def test_salary_req_attr():
    tl = TeamLead("Tom", 4000, "Panel_team", "Python", 13)
    assert hasattr(tl, "salary"), "There is No \"salary\" attribute!"


# Альтернативні тести через parametrize
@pytest.mark.parametrize("attr,exp_res",
                         [("department", True),
                          ("programming_language", True),
                          ("team_size", True),
                          ("team", False),
                          ("name", True),
                          ("surname", False),
                          ("salary", True)])
def test_req_attr(team_lead, attr, exp_res):
    act_res = hasattr(team_lead, attr)
    assert act_res == exp_res


# Тут я додатково вирішив ще перевірити правильність типів атрибутів
@pytest.mark.parametrize("attr_name,default,exp_type,exp_res",
                         [("department", None, str, "Panel_team"),
                          ("programming_language", None, str, "Python"),
                          ("team_size", 0, int, 13),
                          ("team", None, str, None),
                          ("salary", 0, int, 4000),
                          ("surname", None, str, None),
                          ("name", None, str, "Tom")])
def test_get_attr(team_lead, attr_name, default, exp_type, exp_res):
    assert get_attr(team_lead, attr_name, default, exp_type) == exp_res
