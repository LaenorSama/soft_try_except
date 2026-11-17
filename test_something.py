import allure
import pytest
import traceback

from func import *

@allure.title("Автотест")
@allure.label("owner", "Alex")
def test_auto_with_soft_try_except():
    errors = []
    skipped = []

    # Шаг 1 - 100% выполнение
    with allure.step("Первый шаг"):
        pass

    # Шаг 2 - 100% падение с мягким try/except
    try:
        with allure.step("Второй шаг"):
            safe_lucky_step(1)
    except RuntimeWarning as e:  # skip
        allure.attach(str(e), name="Шаг пропущен", attachment_type=allure.attachment_type.TEXT)
        skipped.append(str(e))
    except Exception as e:  # fail/broken
        tb = traceback.format_exc()
        allure.attach(tb, name="Ошибка во втором шаге", attachment_type=allure.attachment_type.TEXT)
        errors.append(tb)

    # Шаг 3 - 100% выполнение
    with allure.step("Третий шаг"):
        pass

    # Итоговое состояние теста
    if errors:
        allure.attach("\n\n".join(errors), name="Ошибки шагов", attachment_type=allure.attachment_type.TEXT)
        pytest.fail("Есть ошибки в шагах", pytrace=False)

    elif skipped:
        allure.attach("\n\n".join(skipped), name="Пропущенные шаги", attachment_type=allure.attachment_type.TEXT)
        pytest.skip("Некоторые шаги были пропущены")

import allure
import pytest


@allure.id("3105")
@allure.title("Ручной тест-кейс 2")
@allure.label("owner", "Alex")
# Тест 100% выполнится со всеми шагами
def test_manual_to_auto():
    allure.dynamic.label("suite", "test_something");
    with allure.step("Первый шаг ручного теста"):
        pass
    with allure.step("Второй шаг ручного теста"):
        pass
    with allure.step("Третий шаг ручного теста"):
        pass

import allure
import pytest


@allure.id("3110")
@allure.title("Ручной тест-кейс 1")
@allure.label("owner", "Alex")
# Тест 100% упадет на шаге 2, шаг 3 не попадет в результат
def test_manual_to_auto2():
    allure.dynamic.label("suite", "test_something");
    with allure.step("Первый шаг ручного теста"):
        pass
    with allure.step("Второй шаг ручного теста"):
        lucky_step(1)
        pass
    with allure.step("Третий шаг ручного теста"):
        pass

# Пустой автотест
def test_autotest_empty():
    pass