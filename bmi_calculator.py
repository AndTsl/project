# bmi_calculator.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Рассчитывает индекс массы тела (ИМТ).
    
    :param weight_kg: Вес в килограммах (должен быть > 0)
    :param height_m: Рост в метрах (должен быть > 0)
    :return: ИМТ, округлённый до 2 знаков
    :raises ValueError: Если вес или рост <= 0
    """
    if weight_kg <= 0:
        raise ValueError("Вес должен быть положительным числом.")
    if height_m <= 0:
        raise ValueError("Рост должен быть положительным числом.")
    
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2) 
