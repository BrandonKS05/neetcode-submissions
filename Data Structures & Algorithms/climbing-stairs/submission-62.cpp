class Solution {
public:
    int climbStairs(int n) {
        // recursive method;
        //  so we just want to go send out our minions to do work for us
        // so we send someone to do our fib(n-1) work and then add our fib(n-2) work as well
        // however we will notice that the work will begin to overlap and become what we may call
        // "redundant'" ' basically we have overlapping subproblems 
        // the branches aren't aware of one another thus we need a general billboard or you may
        // "communal memory"
        // basically we are enforcing state
        //so our functino would look somthing like this:
        // base case: if n == 1 --> equal to 1
        // recursive code: return fib(n-1) + fib(n-2)
        //but this is just our stupid infinity runtime solution
        // we need state-ness
        // id' rather solve itearvely but i can't
        //
        // k = n and v = fib(n)



        unordered_map<int, int> billboard;
        auto fib = [=](this auto&& fib, int n) -> int {
            if(n <= 2) return n;

            if (billboard.contains(n)) return billboard[n];

            billboard[n] = fib(n - 1) + fib(n - 2);

            return billboard[n];
          };
   
    return fib(n);
    }
};

