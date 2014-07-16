vector<int> postorderTraversal(TreeNode *root) {
    vector<int> output;
    if(root){
        stack<TreeNode *> nodeStack;
        stack<TreeNode *> vistedStack;
        nodeStack.push(root);
        while(!nodeStack.empty()){
            struct TreeNode *node=nodeStack.top();
            vistedStack.push(node);
            nodeStack.pop();
            if(node->left)
                nodeStack.push(node->left);
            if(node->right)
                nodeStack.push(node->right);
            }
        while(!vistedStack.empty()){
            output.push_back(vistedStack.top()->val);
            vistedStack.pop();
        }
    }
    return output;
}
