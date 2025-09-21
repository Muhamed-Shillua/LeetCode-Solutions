class Solution {
public:
    int reverse(int x) 
    {
        int y = 0;
        int z = 0;
        bool negative = x<0;
        if (x == INT_MIN)
        {
            return 0;
        }
        x = abs(x);
        while (x > 0)
        {
            z = x % 10;                   
            x = x / 10;
            if (y > INT_MAX / 10 || (y == INT_MAX / 10 && z > 7)) 
            {
                return 0;
            }                            
            y = (y * 10) + z;              
        }
        return (negative)? (y*-1):y;
        
    }
};