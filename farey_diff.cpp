#include <cmath>
#include <cstdio>
#include <vector>

namespace {

std::vector<std::tuple<int, int>> factor(int n) {
    std::vector<std::tuple<int, int>> out;
    for (int i = 2; n > 1; i++) {
        int e = 0;
        while (n % i == 0) {
            n /= i;
            e++;
        }
        if (e > 0) out.push_back({i, e});
    }
    return out;
}

int totient(int n) {
    int out = 1;
    for (auto f: factor(n)) {
        auto [p, e] = f;
        int a = 1;
        for (int i = 0; i < e - 1; i++) {
            a *= p;
        }
        out *= a * (p - 1);
    }
    return out;
}

std::vector<double> farey_diff(int n) {
    // In the end, we just wanted a cumsum...
    std::vector<int> tots(n + 1);
    tots[0] = 0;
    for (int i = 1; i <= n; i++) tots[i] = totient(i);
    std::vector<int> tots1(n + 1);
    tots1[0] = 0;
    for (int i = 1; i <= n; i++) tots1[i] = tots1[i - 1] + tots[i];
    int Fn = tots1.back();
    // ...but we did this.
    std::vector<long> farey_num(1 + Fn / 2), farey_den(1 + Fn / 2);
    std::tie(farey_num[0], farey_den[0]) = std::make_tuple(0, 1);
    std::tie(farey_num[1], farey_den[1]) = std::make_tuple(1, n);
    for (int i = 2; i <= Fn / 2; i++) {
        auto [a, b] = std::make_tuple(farey_num[i - 2], farey_den[i - 2]);
        auto [c, d] = std::make_tuple(farey_num[i - 1], farey_den[i - 1]);
        int k = (n + b) / d;
        farey_num[i] = k * c - a;
        farey_den[i] = k * d - b;
    }
    std::vector<int> tots2(n + 1, 0);
    std::vector<double> df(n + 1, 0);
    for (int i = 1; i < Fn / 2; i++) {
        auto [a, b] = std::make_tuple(farey_num[i], farey_den[i]);
        for (int j = b; j <= n; j++) {
            tots2[j]++;
            auto [c, d] = std::make_tuple(tots2[j], tots1[j]);
            df[j] += std::abs(double(a * d - b * c) / (b * d));
        }
    }
    for (int i = 1; i <= n; i++) df[i] *= 2;
    return df;
}

}

int main() {
    auto df = farey_diff(5000);
    for (int i = 1; i <= 5000; i++) {
        printf("%4d %f\n", i, df[i]);
    }
}
