class Solution{
    bool leaf =false;
public:
    bool isComplete(TreeNode* root){
        if(root=NULL) return true;
        queue<TreeNode*> mq;
        mq.push(root);
        while(!mq.emptyy()){
            int n=mq.size();
            for (int i=0;i<n;i++){
                TreeNode *node=mq.front();
                if(leaf && (node->left!=NULL ||node->right!=NULL))return false;
                if(node->left==NULL ||node->right==NULL) leaf=true;
                if(node->left==NULL &&node->right!=NULL) return false;
                if(node->left) mq.push(node->left);
                if(node->right) mq.push(node->right);
                mq.pop();
            }
        }
        return true;

    }

}
