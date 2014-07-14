vector<int> preorderTraversal(TreeNode *root) {
        vector<int> output;
        if(root==NULL){
            
            return output;
        }
        
        stack<TreeNode *> nodeStack;
        nodeStack.push(root);
        
        while(nodeStack.empty()==false){
            struct TreeNode *node=nodeStack.top();
            output.push_back(node->val);
            nodeStack.pop();
            
            if(node->right!=NULL){
                nodeStack.push(node->right);
            }
            if(node->left!=NULL){
                nodeStack.push(node->left);
            }
        }
        
        return output;
    }
