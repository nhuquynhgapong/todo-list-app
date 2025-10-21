tasks = []

def add_task(name: str):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(name)

def list_tasks():
    """
    if not tasks:
        print("Chưa có công việc nào.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    # Demo theo yêu cầu: gọi list_tasks() sau khi đã thêm xong công việc
    add_task("Học bài Git")
    add_task("Làm bài tập")
    list_tasks()
