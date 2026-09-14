# Python & Git 기초
# 나만의 프롬프트 관리 프로그램


# 미리 정의한 카테고리
CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
]


# 이전 AI 미션에서 실제로 사용한 기본 프롬프트
prompts = [
    {
        "title": "몸 이상 신호 기반 컬러푸드 서비스 기획",
        "content": (
            "내 몸이 보내는 이상 신호에 따른 음식 추천으로 과제를 수행하고자 해. "
            "대표적인 과일을 색깔별로 하나 이상 추천하는데, 많이 복잡하고 비용이 들지 않다면, "
            "페이지 또는 섹션(메뉴 이동 가능)을 15개 정도 해도 괜찮아. "
            "어떤지 생각한 뒤 의견 알려줘.\n\n"
            "보너스 과제는 돈이 안 들면서, 구현하면 좋은 "
            "(권장되는 기능만 구현해도 됨.)"
        ),
        "category": "텍스트 생성",
        "favorite": False,
        "view_count": 0,
    },
    {
        "title": "주식투자 위험 영상 이미지 수정",
        "content": (
            "사진을 보면 영상 속에 남자 뒤에 돈이 쌓여 있어. "
            "주식투자의 위험성을 알리려고 하는데, 돈을 번 것 같아. "
            "그래서 뒤에 돈다발을 없애줘. "
            "그리고 글자를 알아볼 수 없는 문서를 보고 있는데, "
            "그 문서를 차용증으로 바꿔줘.\n\n"
            "수정한 이유? 배경에 한국 원화 돈다발이 쌓여 있습니다. "
            "이 사진은 '돈' 그 자체에 집중하게 만들며, "
            "긍정적이거나 단순히 재정적인 상황을 암시할 수 있습니다."
        ),
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0,
    },
    {
        "title": "결과 캐싱 개념 설명",
        "content": (
            "보너스 2 — 결과 캐싱\n\n"
            "16-1. 구현 목적\n\n"
            "[여기에 작성]\n\n"
            "힌트: 같은 날짜로 반복 실행할 때 불필요한 API 비용과 실행 시간을 "
            "줄이기 위해 구현했다고 적으세요.\n\n"
            "결과 캐싱이라고 하면 뭐지? 하는 사람들이 있음."
        ),
        "category": "텍스트 생성",
        "favorite": False,
        "view_count": 0,
    },
    {
        "title": "복수 여행지 증빙 확인",
        "content": (
            "복수 여행지 추천은 지역이 3개가 보여야 하는데, "
            "증빙 사진이 제대로 들어간 게 맞는지?"
        ),
        "category": "기타",
        "favorite": False,
        "view_count": 0,
    },
]


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정 [Bonus]")
    print("9. 프롬프트 삭제 [Bonus]")
    print("10. 많이 본 프롬프트 Top 5 [Bonus]")
    print("0. 종료")


def get_non_empty_input(message):
    """빈 값을 허용하지 않고 입력을 반복해서 받는다."""
    while True:
        try:
            value = input(message).strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if value:
            return value

        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def select_category():
    """프롬프트 추가 또는 수정 시 카테고리를 선택하거나 직접 입력한다."""
    print("\n카테고리를 선택하세요.")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    print("0. 직접 입력")

    while True:
        try:
            choice = input("선택: ").strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if choice == "0":
            category = get_non_empty_input("카테고리 직접 입력: ")

            if category is None:
                return None

            return category

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]

        print("잘못된 카테고리 번호입니다. 다시 입력해주세요.")


def add_prompt():
    """새로운 프롬프트를 추가한다."""
    print("\n=== 프롬프트 추가 ===")

    title = get_non_empty_input("제목: ")
    if title is None:
        print("\n프롬프트 추가를 취소합니다.")
        return

    content = get_non_empty_input("내용: ")
    if content is None:
        print("\n프롬프트 추가를 취소합니다.")
        return

    category = select_category()
    if category is None:
        print("\n프롬프트 추가를 취소합니다.")
        return

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "view_count": 0,
    }

    prompts.append(new_prompt)

    print("\n프롬프트가 추가되었습니다.")
    print(f"제목: {title}")
    print(f"카테고리: {category}")
    print("즐겨찾기: ☆")
    print("조회수: 0")


def show_prompt_list():
    """등록된 프롬프트 목록을 번호, 제목, 카테고리, 즐겨찾기와 함께 출력한다."""
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else "☆"

        print(
            f"{index}. "
            f"{favorite_mark} "
            f"{prompt['title']} "
            f"[{prompt['category']}]"
        )


def get_available_categories():
    """기본 카테고리와 사용자가 직접 추가한 카테고리를 함께 반환한다."""
    categories = CATEGORIES.copy()

    for prompt in prompts:
        category = prompt["category"]

        if category not in categories:
            categories.append(category)

    return categories


def select_category_for_filter():
    """카테고리별 조회에 사용할 카테고리를 선택한다."""
    categories = get_available_categories()

    print("\n조회할 카테고리를 선택하세요.")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = input("선택: ").strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(categories):
                return categories[number - 1]

        print("잘못된 카테고리 번호입니다. 다시 입력해주세요.")


def show_prompts_by_category():
    """선택한 카테고리에 해당하는 프롬프트만 출력한다."""
    category = select_category_for_filter()

    if category is None:
        print("\n카테고리별 조회를 취소합니다.")
        return

    filtered_prompts = [
        prompt
        for prompt in prompts
        if prompt["category"] == category
    ]

    if not filtered_prompts:
        print(f"\n'{category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n=== {category} 카테고리 ===")

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else "☆"

        print(
            f"{index}. "
            f"{favorite_mark} "
            f"{prompt['title']}"
        )


def search_prompts():
    """제목 또는 내용에 검색어가 포함된 프롬프트를 찾는다."""
    print("\n=== 프롬프트 검색 ===")

    keyword = get_non_empty_input("검색어: ")

    if keyword is None:
        print("\n프롬프트 검색을 취소합니다.")
        return

    normalized_keyword = keyword.casefold()

    search_results = [
        prompt
        for prompt in prompts
        if normalized_keyword in prompt["title"].casefold()
        or normalized_keyword in prompt["content"].casefold()
    ]

    if not search_results:
        print(f"\n'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print(f"\n=== '{keyword}' 검색 결과 ===")

    for index, prompt in enumerate(search_results, start=1):
        favorite_mark = "★" if prompt["favorite"] else "☆"

        print(
            f"{index}. "
            f"{favorite_mark} "
            f"{prompt['title']} "
            f"[{prompt['category']}]"
        )


def show_prompt_detail():
    """선택한 프롬프트의 상세 정보를 출력하고 조회수를 1 증가시킨다."""
    if not prompts:
        print("\n등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    while True:
        try:
            choice = input("\n상세 보기할 프롬프트 번호: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n프롬프트 상세 보기를 취소합니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                prompt["view_count"] += 1
                favorite_mark = "★" if prompt["favorite"] else "☆"

                print("\n=== 프롬프트 상세 정보 ===")
                print(f"번호: {number}")
                print(f"제목: {prompt['title']}")
                print(f"카테고리: {prompt['category']}")
                print(f"즐겨찾기: {favorite_mark}")
                print(f"조회수: {prompt['view_count']}")
                print("내용:")
                print(prompt["content"])
                return

        print("잘못된 프롬프트 번호입니다. 다시 입력해주세요.")


def toggle_favorite():
    """선택한 프롬프트의 즐겨찾기 상태를 변경한다."""
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    while True:
        try:
            choice = input("\n즐겨찾기를 변경할 프롬프트 번호: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n즐겨찾기 관리를 취소합니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                prompt["favorite"] = not prompt["favorite"]

                favorite_mark = "★" if prompt["favorite"] else "☆"
                favorite_state = (
                    "즐겨찾기에 추가되었습니다."
                    if prompt["favorite"]
                    else "즐겨찾기에서 해제되었습니다."
                )

                print(f"\n제목: {prompt['title']}")
                print(f"즐겨찾기: {favorite_mark}")
                print(favorite_state)
                return

        print("잘못된 프롬프트 번호입니다. 다시 입력해주세요.")


def show_favorites():
    """즐겨찾기된 프롬프트만 전체 목록의 원래 번호와 함께 출력한다."""
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = [
        (index, prompt)
        for index, prompt in enumerate(prompts, start=1)
        if prompt["favorite"]
    ]

    if not favorite_prompts:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for original_number, prompt in favorite_prompts:
        print(
            f"{original_number}. "
            f"★ "
            f"{prompt['title']} "
            f"[{prompt['category']}]"
        )


def edit_prompt():
    """선택한 프롬프트의 제목, 내용, 카테고리를 수정한다."""
    print("\n=== 프롬프트 수정 [Bonus] ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    while True:
        try:
            choice = input("\n수정할 프롬프트 번호: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n프롬프트 수정을 취소합니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                selected_number = number
                prompt = prompts[selected_number - 1]
                break

        print("잘못된 프롬프트 번호입니다. 다시 입력해주세요.")

    print("\n현재 정보")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print("내용:")
    print(prompt["content"])

    print("\n새로운 정보를 입력하세요.")

    title = get_non_empty_input("새 제목: ")
    if title is None:
        print("\n프롬프트 수정을 취소합니다.")
        return

    content = get_non_empty_input("새 내용: ")
    if content is None:
        print("\n프롬프트 수정을 취소합니다.")
        return

    category = select_category()
    if category is None:
        print("\n프롬프트 수정을 취소합니다.")
        return

    prompt["title"] = title
    prompt["content"] = content
    prompt["category"] = category

    print("\n프롬프트가 수정되었습니다.")
    print(f"번호: {selected_number}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'★' if prompt['favorite'] else '☆'}")
    print(f"조회수: {prompt['view_count']}")


def delete_prompt():
    """선택한 프롬프트를 확인 후 삭제한다."""
    print("\n=== 프롬프트 삭제 [Bonus] ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    while True:
        try:
            choice = input("\n삭제할 프롬프트 번호: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n프롬프트 삭제를 취소합니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                selected_number = number
                prompt = prompts[selected_number - 1]
                break

        print("잘못된 프롬프트 번호입니다. 다시 입력해주세요.")

    print("\n삭제 대상")
    print(f"번호: {selected_number}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")

    while True:
        try:
            confirm = input("정말 삭제하시겠습니까? (y/n): ").strip().casefold()
        except (EOFError, KeyboardInterrupt):
            print("\n프롬프트 삭제를 취소합니다.")
            return

        if confirm == "y":
            deleted_prompt = prompts.pop(selected_number - 1)
            print(f"\n'{deleted_prompt['title']}' 프롬프트가 삭제되었습니다.")
            return

        if confirm == "n":
            print("\n프롬프트 삭제를 취소했습니다.")
            return

        print("y 또는 n을 입력해주세요.")


def show_top_prompts():
    """상세 보기 조회수가 높은 프롬프트를 최대 5개까지 출력한다."""
    print("\n=== 많이 본 프롬프트 Top 5 [Bonus] ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    viewed_prompts = [
        (index, prompt)
        for index, prompt in enumerate(prompts, start=1)
        if prompt["view_count"] > 0
    ]

    if not viewed_prompts:
        print("아직 상세 보기 기록이 없습니다.")
        return

    sorted_prompts = sorted(
        viewed_prompts,
        key=lambda item: item[1]["view_count"],
        reverse=True,
    )

    top_prompts = sorted_prompts[:5]

    for rank, (original_number, prompt) in enumerate(top_prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else "☆"

        print(
            f"{rank}위. "
            f"{favorite_mark} "
            f"{prompt['title']} "
            f"[{prompt['category']}] "
            f"- 원본 번호: {original_number}, "
            f"조회수: {prompt['view_count']}"
        )


def main():
    """사용자가 종료를 선택할 때까지 메인 메뉴를 반복 실행한다."""
    while True:
        show_menu()

        try:
            choice = input("선택: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n프로그램을 종료합니다.")
            break

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_prompt_list()

        elif choice == "3":
            show_prompts_by_category()

        elif choice == "4":
            search_prompts()

        elif choice == "5":
            show_prompt_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "8":
            edit_prompt()

        elif choice == "9":
            delete_prompt()

        elif choice == "10":
            show_top_prompts()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
