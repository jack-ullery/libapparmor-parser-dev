#ifndef RULE_NODE_HH
#define RULE_NODE_HH

#include "TreeNode.hh"
#include "tree/PrefixNode.hh"
#include <cstdint>
#include <string>

class RuleNode : public TreeNode {
  public:
    RuleNode();
    RuleNode(uint64_t startPos, uint64_t stopPos);
    RuleNode(const std::string &text, uint64_t startPos, uint64_t stopPos);

    uint64_t getStartPosition() const;
    uint64_t getStopPosition()  const;

    void setPrefix(PrefixNode &prefix);

  protected:
    PrefixNode prefix;

    uint64_t startPos;
    uint64_t stopPos;
};

#endif // RULE_NODE_HH