#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  auto findRepeatedDnaSequences(std::string s) -> std::vector<std::string> {
    // Here, n is the length of the input string
    const auto n = static_cast<int>(s.length());

    // We should store how many times we have seen something
    //
    // This ensures we don't add to our result over once without
    // constructing an extra set
    auto sequencesSeen = std::unordered_map<std::string, size_t>();

    // And store our final answer
    auto repeatedSequences = std::vector<std::string>();

    // Loop through all substrings of length 10.
    for (int l = 0; l <= n - 10; ++l) {
      // Get a length 10 substring starting at l.
      auto substr = s.substr(l, 10);

      // Get a reference to the appearance count for that
      // substring.
      auto &count = sequencesSeen[substr];

      // We have now seen that substring. Increment count.
      count++;

      // If this is exactly the second time we have seen it,
      // add the substring to our result.
      if (count == 2)
        repeatedSequences.push_back(substr);
    }

    return repeatedSequences;
  }
};
