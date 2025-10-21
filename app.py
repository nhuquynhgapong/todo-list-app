tasks = []  # ví dụ: ["Học Git", "Làm bài tập"]

def add_task(name: str):
    tasks.append(name)

def list_tasks():
    if not tasks:
        print("Chưa có công việc nào.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(task_index):

    # Cho phép truyền string số => ép về int
    try:
        idx = int(task_index)
    except ValueError:
        print("Chỉ số phải là số nguyên dương.")
        return False

    if idx < 1 or idx > len(tasks):
        print("Chỉ số không hợp lệ.")
        return False

    removed = tasks.pop(idx - 1)
    print(f"Đã xoá: {removed}")
    return True

if __name__ == "__main__":
    # Demo ngắn
    add_task("Học bài Git")
    add_task("Làm bài tập")
    add_task("Đi chợ")

    print("Trước khi xoá:")
    list_tasks()

    delete_task(2)  # xoá mục số 2: "Làm bài tập"

    print("\nSau khi xoá:")
    list_tasks()
