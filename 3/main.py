import random


class NinjaKradzionyAgent:
    """⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠴⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠠⠶⠶⠶⠶⢶⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
    ⠀⠀⠀⠀⢀⣴⣶⣶⣶⣶⣶⣶⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
    ⠀⠀⠀⠀⣸⣿⡿⠟⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠿⣿⣿⡄⠀
    ⠀⠀⠀⠀⣿⠋⠀⠀⠀⠐⢶⣶⣶⠆⠀⠀⠀⠀⠀⢶⣶⣶⠖⠂⠀⠀⠈⢻⡇⠀
    ⠀⠀⠀⠀⢹⣦⡀⠀⠀⠀⠀⠉⢁⣠⣤⣶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⣀⣾⠃⠀
    ⠀⠀⠀⠀⠘⣿⣿⣿⣶⣶⣶⣾⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣷⣶⣾⣿⣿⡿⠀⠀
    ⠀⠀⢀⣴⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
    ⠀⠀⣾⡿⢃⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
    ⠀⢸⠏⠀⣿⡇⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀
    ⠀⠀⠀⢰⣿⠃⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⣉⣁⣤⡶⠁⠀⠀⠀⠀⠀
    ⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
                    かかって来い!"""

    def __init__(OOOO000O000O00000):
        OOOO000O000O00000.numbers = []

    def act(O000000O000OO0O0O, vector: list):
        if len(vector) % 2 == 0:
            sum_even = sum(vector[::2])
            sum_odd = sum(vector) - sum_even
            if sum_even >= sum_odd:
                O000000O000OO0O0O.numbers.append(vector[0])
                return vector[1:]  # explained: https://r.mtdv.me/articles/k1evNIASMp
            O000000O000OO0O0O.numbers.append(vector[-1])
            return vector[:-1]
        else:
            sum_even = max(sum(vector[1::2]), sum(vector[2::2]))
            sum_odd = max(sum(vector[:-1:2]), sum(vector[:-2:2]))
            if sum_even >= sum_odd:
                O000000O000OO0O0O.numbers.append(vector[-1])
                return vector[:-1]
            O000000O000OO0O0O.numbers.append(vector[0])
            return vector[1:]


# random.seed(8)  # TODO: For final results set seed as your student's id modulo 42

# def choose(self, vector: list, isMine, depth):
#         if len(vector) > 1:
#             bilans_first = self.choose(vector[1:], not isMine, depth - 1)
#             bilans_last = self.choose(vector[:-1], not isMine, depth - 1)
#             if isMine:
#                 bilans_first += vector[0]
#                 bilans_last += vector[-1]
#             else:
#                 bilans_first -= vector[0]
#                 bilans_last -= vector[-1]

#             if isMine:
#                 bilans = max(bilans_first, bilans_last)
#             else:
#                 bilans = min(bilans_first, bilans_last)


#             return bilans
#         else:
#             if isMine:
#                 return max(vector[0], vector[-1])
#             else:
#                 return -max(vector[0], vector[-1])
class RandomAgent:
    def __init__(self):
        self.numbers = []

    def act(self, vector: list):
        if random.random() > 0.5:
            self.numbers.append(vector[0])
            return vector[1:]
        self.numbers.append(vector[-1])
        return vector[:-1]


class GreedyAgent:
    def __init__(self):
        self.numbers = []

    def act(self, vector: list):
        if vector[0] > vector[-1]:
            self.numbers.append(vector[0])
            return vector[1:]
        self.numbers.append(vector[-1])
        return vector[:-1]


class MinMaxAgent:
    def __init__(self, max_depth=50):
        self.numbers = []
        self.depth = max_depth

    def choose(self, vector: list, isMine, depth):
        if len(vector) > 1:
            bilans_first = self.choose(vector[1:], not isMine, depth - 1)
            bilans_last = self.choose(vector[:-1], not isMine, depth - 1)
            if isMine:
                bilans_first += vector[0]
                bilans_last += vector[-1]
            else:
                bilans_first -= vector[0]
                bilans_last -= vector[-1]
            if isMine:
                bilans = max(bilans_first, bilans_last)
            else:
                bilans = min(bilans_first, bilans_last)

            return bilans
        else:
            if isMine:
                return max(vector[0], vector[-1])
            else:
                return -max(vector[0], vector[-1])

    def act(self, vector: list):
        depth = self.depth
        isMine = True
        if len(vector) > 1:
            bilans_first = self.choose(vector[1:], not isMine, depth - 1)
            bilans_last = self.choose(vector[:-1], not isMine, depth - 1)
            bilans_first += vector[0]
            bilans_last += vector[-1]
            if bilans_first > bilans_last:
                self.numbers.append(vector[0])
                return vector[1:]
            else:
                self.numbers.append(vector[-1])
                return vector[:-1]
        else:
            self.numbers.append(vector[0])
            return vector[1:]


class NinjaAgent:
    """⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠴⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠠⠶⠶⠶⠶⢶⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
    ⠀⠀⠀⠀⢀⣴⣶⣶⣶⣶⣶⣶⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
    ⠀⠀⠀⠀⣸⣿⡿⠟⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠿⣿⣿⡄⠀
    ⠀⠀⠀⠀⣿⠋⠀⠀⠀⠐⢶⣶⣶⠆⠀⠀⠀⠀⠀⢶⣶⣶⠖⠂⠀⠀⠈⢻⡇⠀
    ⠀⠀⠀⠀⢹⣦⡀⠀⠀⠀⠀⠉⢁⣠⣤⣶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⣀⣾⠃⠀
    ⠀⠀⠀⠀⠘⣿⣿⣿⣶⣶⣶⣾⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣷⣶⣾⣿⣿⡿⠀⠀
    ⠀⠀⢀⣴⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
    ⠀⠀⣾⡿⢃⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
    ⠀⢸⠏⠀⣿⡇⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀
    ⠀⠀⠀⢰⣿⠃⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⣉⣁⣤⡶⠁⠀⠀⠀⠀⠀
    ⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
                    かかって来い!"""

    def __init__(OOOO000O000O00000):
        OOOO000O000O00000.numbers = []

    def act(O000000O000OO0O0O, O0OO0O0O0O0OO0O00: list):
        if len(O0OO0O0O0O0OO0O00) % 2 == 0:
            O00O0O0000000OO0O = sum(O0OO0O0O0O0OO0O00[::2])
            O0O00O0OO00O0O0O0 = sum(O0OO0O0O0O0OO0O00) - O00O0O0000000OO0O
            if O00O0O0000000OO0O >= O0O00O0OO00O0O0O0:
                O000000O000OO0O0O.numbers.append(O0OO0O0O0O0OO0O00[0])
                return O0OO0O0O0O0OO0O00[
                    1:
                ]  # explained: https://r.mtdv.me/articles/k1evNIASMp
            O000000O000OO0O0O.numbers.append(O0OO0O0O0O0OO0O00[-1])
            return O0OO0O0O0O0OO0O00[:-1]
        else:
            O00O0O0000000OO0O = max(
                sum(O0OO0O0O0O0OO0O00[1::2]), sum(O0OO0O0O0O0OO0O00[2::2])
            )
            O0O00O0OO00O0O0O0 = max(
                sum(O0OO0O0O0O0OO0O00[:-1:2]), sum(O0OO0O0O0O0OO0O00[:-2:2])
            )
            if O00O0O0000000OO0O >= O0O00O0OO00O0O0O0:
                O000000O000OO0O0O.numbers.append(O0OO0O0O0O0OO0O00[-1])
                return O0OO0O0O0O0OO0O00[:-1]
            O000000O000OO0O0O.numbers.append(O0OO0O0O0O0OO0O00[0])
            return O0OO0O0O0O0OO0O00[1:]


def run_game(vector, first_agent, second_agent):
    while len(vector) > 0:
        vector = first_agent.act(vector)
        if len(vector) > 0:
            vector = second_agent.act(vector)


def main():
    win_m = 0
    win_n = 0
    seed = 0
    job_seed = 0
    for _ in range(1000):
        random.seed(seed)
        vector = [random.randint(-10, 10) for _ in range(4)]
        # print(f"Vector: {vector}")
        first_agent, second_agent = MinMaxAgent(), NinjaAgent()
        run_game(vector, first_agent, second_agent)

        # print(
        #     f"First agent: {sum(first_agent.numbers)} Second agent: {sum(second_agent.numbers)}\n"
        #     f"First agent: {first_agent.numbers}\n"
        #     f"Second agent: {second_agent.numbers}"
        # )
        if sum(first_agent.numbers) > sum(second_agent.numbers):
            win_m += 1
        elif sum(first_agent.numbers) < sum(second_agent.numbers):
            win_n += 1
            job_seed = seed
        seed += 1
    print(vector)
    print(first_agent.numbers)
    print(second_agent.numbers)
    print(win_m)
    print(win_n)
    print(job_seed)


if __name__ == "__main__":
    main()
