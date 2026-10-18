"""
student_utils.py
包含学生成绩解析工具函数。
"""

def parse_student(line):
    """解析一行学生记录，返回字典；无效抛出 ValueError。"""
    line = line.strip()
    parts = line.split(",")

    if len(parts) != 2:
        raise ValueError(f"字段数量错误：期望 2 个，实际 {len(parts)} 个")

    name, score_str = parts

    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是数字：'{score_str}'")

    if score < 0 or score > 100:
        raise ValueError(f"成绩超出范围：{score}")

    return {"name": name, "score": score}