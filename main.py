from Tests.login import login_tests
from Tests.uteis import get_data_test
from Tests.forgot_password import forgot_password_tests
from Tests.activity import activity_tests

url = "https://growth-station-client-git-junk-teste-qa-growthmachine.vercel.app/login"

def login():
    massa = get_data_test("Massas", "login_tests.json")

    result = login_tests(url, massa)
    if isinstance(result, tuple) and len(result) == 2:
        success, failed = result

        print("[Login tests] sucesso: ", len(success))
        print("[Login tests] erro: ", len(failed))

        if len(failed) > 0:
            print("[Login tests] Detalhes dos erros", failed)

def forgot_password():
    massa = get_data_test("Massas", "forgot_password_tests.json")
    success, failed = forgot_password_tests(url, massa)

    print("[Forgot Password tests] sucesso: ", len(success))
    print("[Forgot Password tests] erro: ", len(failed))

    if len(failed) > 0:
        print("[Forgot Password tests] Detalhes dos erros", failed)

def activity():
    massa = get_data_test("Massas", "activity_tests.json")
    success, failed = activity_tests(url, massa)

    print("[Forgot Password tests] sucesso: ", len(success))
    print("[Forgot Password tests] erro: ", len(failed))

    if len(failed) > 0:
        print("[Activity tests] Detalhes dos erros", failed)

def run_tests():
    #login()
    #forgot_password()
    activity()

run_tests()
