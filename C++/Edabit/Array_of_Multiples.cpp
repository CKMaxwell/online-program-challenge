//20200917 - Array of Multiples
#include <vector>

std::vector<int> arrayOfMultiples(int num, int length) {
	int ans[length];
	for (int i = 1;i<=length;i++)
	{
		ans[i] = num*i;
	}
	return ans;
}
