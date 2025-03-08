#Part 1
#Problems 1: Password
# Sử dụng Hoán vị bằng thử viện itertools
from itertools import permutations

# Hàm để kiểm tra xem mật khẩu có thoả điều kiện đã cho hay không
def is_valid_password(password, clues):
    for clue in clues:
        guess = clue[0]
        correct = clue[1]
        correct_pos = clue[2]

        correct_count = sum(1 for i in range(3) if password[i] == guess[i])
        if correct_count != correct_pos:
            return False

        total_correct = sum(1 for digit in password if digit in guess)
        if total_correct - correct_count != correct:
            return False

    return True

# Đưa ra một số giả thiết
clues = [
    ("472", 1, 0),
    ("581", 1, 0),
    ("483", 1, 1),
    ("317", 2, 0),
    ("956", 0, 0)
]

# Tạo hoán vị từ ba chữ số riêng biệt từ 1 đến 9 
possible_passwords = [''.join(p) for p in permutations('123456789', 3)]

# Lặp lại toàn bộ mật khẩu có thể xảy ra và kiểm tra từng mật khẩu một
for password in possible_passwords:
    if is_valid_password(password, clues):
        print("Problem 1 - The password is:", password)
        break

#Part 3
#Problems 5: Symbolic form
def symbolic_forms(abcd):
    p = "it is windy"
    q = "it is thundering"
    r = "it is raining"
    s = "it is lightning"

    even_statements = ["a", "d", "f", "g"]
    odd_statements = ["b", "c", "e", "g"]

    if abcd % 2 == 0:
        statements = even_statements
    else:
        statements = odd_statements

    symbolic_forms = []

    for statement in statements:
        if statement == "a":
            # It is windy but it isn't raining
            symbolic_forms.append(f"{p} ∧ ~{r}")
        elif statement == "b":
            # It is windy, thundering but it isn't raining
            symbolic_forms.append(f"{p} ∧ {q} ∧ ~{r}")
        elif statement == "c":
            # It is raining without thundering and lightning
            symbolic_forms.append(f"{r} ∧ ~{q} ∧ ~{s}")
        elif statement == "d":
            # Windiness is a necessary condition for rain
            symbolic_forms.append(f"{p} → {r}")
        elif statement == "e":
            # Windiness is a sufficient condition for rain
            symbolic_forms.append(f"{p} → {r}")
        elif statement == "f":
            # Whenever it is lightning, it will be thundering
            symbolic_forms.append(f"{s} → {q}")
        elif statement == "g":
            # The necessary and sufficient condition for thundering is lightning
            symbolic_forms.append(f"{q} ↔ {s}")

    return symbolic_forms

# Dùng MSSV của mình
abcd = 52200023
result = symbolic_forms(abcd % 10)

print("\nProblems 5:")
for idx, form in enumerate(result, 1):
    print(f"Statement {idx}: {form}")

#Problems 6:Equivalence
def evaluate_statement(statement, p, q, r):
    # Thay thế các toán tử bằng kí hiệu hoặc chữ
    statement = statement.replace("~", "not ").replace("∧", "and").replace("v", "or").replace("→", "implies").replace("≡", "==")
    return eval(statement)


def truth_table(statement):
    # Tạo tất cả kết hợp cho bảng chân trị của p,q,r
    truth_values = [(p, q, r) for p in [True, False] for q in [True, False] for r in [True, False]]

    # Đánh giá và lưu kết quả
    truth_table = dict(((p, q, r), evaluate_statement(statement, p, q, r)) for p, q, r in truth_values)

    return truth_table


def prove_equivalence(statement1, statement2):
    # Tạo lại bảng chân trị cho 2 bảng
    truth_table1 = truth_table(statement1)
    truth_table2 = truth_table(statement2)

    # Kiểm tra các giá trị chân trị xem có giống nhau hay không
    equivalent = all(truth_table1[key] == truth_table2[key] for key in truth_table1)

    return equivalent


# Sử dụng MSSV
abcd = 52200023
if abcd % 3 == 0:
    statement1 = "~[(~p ∧ ~~q) v ~(p v r)]"
    statement2 = "(r v p) ∧ (~q v p)"
elif abcd % 3 == 1:
    statement1 = "~[(~p v q) v ~(p ∧ ~(p v q))]"
    statement2 = "p ∧ ~(p v q)"
else:
    statement1 = "~(p v ~(q ∧ r)) ∧ ~(~q v (p v q))"
    statement2 = "(r ∧ q) ∧ ~(q v p)"

print("\nProblems 6:")
# Chứng minh sự tương đương bằng 2 phương thức
equivalence_truth_table = prove_equivalence(statement1, statement2)
print("Proving equivalence using truth table:", equivalence_truth_table)

# Chứng minh bằng luật tương đương logic
equivalence_logical_laws = evaluate_statement(f"({statement1}) ≡ ({statement2})", True, True, True)
print("Proving equivalence using logical equivalence laws:", equivalence_logical_laws)