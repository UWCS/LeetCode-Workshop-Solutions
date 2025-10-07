#include <string>
#include <array>

class Solution {
public:
    auto lengthOfLongestSubstring(std::string s) -> int {
        // Using an array here because we only care if a variable is in
        // our window. It has the same effect as an explicit set. We could
        // also use a vector or bitset, but these are compacted and so we
        // cant take references to the underlying (array is not).
        auto seenSet = std::array<bool, 256>{};

        // These represent what is in our window, inclusive.
        auto leftPointer = 0, rightPointer = 0;

        // Our final result.
        auto longestSubstringLength = 0;

        const auto stringLength = static_cast<int>(s.length());

        // Whilst we are in range for our right pointer
        while (rightPointer < stringLength) {
            // Take a reference to whether we can see the right
            // character or not
            auto &isRightChrSeen = seenSet[s[rightPointer]];

            // Whilst it is in we cannot use it in the window
            while (isRightChrSeen) {
                // So remove characters from the left until it
                // satisfies this condition.
                auto &isLeftChrSeen = seenSet[s[leftPointer]];
                isLeftChrSeen = false;
                leftPointer++;
            }

            // Then add the right character to the window.
            isRightChrSeen = true;

            // And recompute the longest length.
            longestSubstringLength = std::max(
                longestSubstringLength, rightPointer - leftPointer + 1);
            rightPointer++;
        }

        return longestSubstringLength;
    }
};

