class Solution {
public:
    void sortColors(vector<int>& nums) {
	    int min = 0;
	    for (int i = 0; i < nums.size() - 1; i++) {
		    min = i; // assume the current index is the smallest
		    for (int j = i + 1; j < nums.size(); j++) {
			    if (nums[j] < nums[min]) {
				min = j; // update min index
			}
		}
		std::swap(nums[min], nums[i]); // swap once per pass
	}
    }
};
