# 陈安方欣
class OneWei(object):
    def __init__(self, m):  # N为节点数  H为肋板高度 K为迭代次数
        self.m = m
        self.N = int(input("level (N)(节点个数):")) + 1
        self.K = int(input("level (K)(迭代次数):"))
        self.H = float(input("level (H)(为肋板高度):"))
        self.delta = [1 for _ in range(self.N)]
        self.dx = self.H / (self.N - 1)

    def acc1(self):  # 一阶精度计算
        for k in range(self.K):
            for n in range(1, self.N):
                if n < self.N - 1:
                    self.delta[n] = (1 / (2 + (self.m ** 2) * (self.dx ** 2))) * (self.delta[n + 1] + self.delta[n - 1])
                else:
                    self.delta[n] = self.delta[n - 1]

    def acc2(self):  # 二阶精度计算
        for k in range(self.K):
            for n in range(1, self.N):
                if n < self.N - 1:
                    self.delta[n] = (1 / (2 + (self.m ** 2) * (self.dx ** 2))) * (self.delta[n + 1] + self.delta[n - 1])
                else:
                    self.delta[n] = (self.delta[n - 1]) / (1 + (self.m ** 2) * (self.dx ** 2) / 2)

    def run(self):
        while 1:
            cha = int(input("请输入精度（1 or 2）："))
            if cha == 1:
                self.acc1()
                break
            elif cha == 2:
                self.acc2()
                break
            else:
                print("输入有误请重新输入")


def main():
    Temp = []
    h = float(input("h = （空气换热系数）"))
    tw = float(input("tw = (肋端温度)"))
    t8 = float(input("t8 = (环境温度)"))
    lam = float(input("lam = （传热系数）"))
    tt = float(input("t* = （肋片厚度）"))
    m = ((2 * h) / (lam * tt)) ** 0.5
    result = OneWei(m)
    result.run()
    for i in range(result.N):
        x = (tw - t8) * result.delta[i] + t8
        Temp.append(x)
    print(Temp)
    input("按任意键关闭！")


if __name__ == '__main__':
    main()
