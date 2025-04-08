# 아래 구문은 테스트용 input.txt 파일을 읽기 위한 것이며, 제출 시 주석 처리하세요.
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러 개의 테스트 케이스가 주어지므로 각각을 처리합니다.
for test_case in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]

    def isPerfect(puzzle):
        def is_valid_block(block):
            nums = [num for num in block if num != 0]
            return len(nums) == len(set(nums))

        # 행 검사
        for row in puzzle:
            if not is_valid_block(row):
                return False

        # 열 검사
        for col in zip(*puzzle):
            if not is_valid_block(col):
                return False

        # 3x3 블럭 검사
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(puzzle[box_row + i][box_col + j])
                if not is_valid_block(block):
                    return False

        return True

    # 출력 포맷: 문제 요구사항에 따라 조정 가능
    result = 1 if isPerfect(graph) else 0
    print(f"#{test_case} {result}")