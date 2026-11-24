class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
         this.stack = new Stack<Integer>();
        this.minStack = new Stack<Integer>();

    }
    
    public void push(int val) {
        this.stack.push(val);

        // handle empty case before peek which throws EmptyStackException
        // at first condition check
        // note: use || not |. || short circuits as long as one is true
        // using | will check both conditions which results in exception.

        if(this.minStack.isEmpty() || this.minStack.peek() >= val){
            this.minStack.push(val);
        }

    }
    
    public void pop() {
        // handle empty case before pop and peep which throws 
        // EmptyStackException

        if(this.stack.empty()) return;
        int popped = this.stack.pop();
        // if minStack is not empty and we are popping off the top
        if(!this.minStack.empty() && this.minStack.peek() == popped){
            this.minStack.pop();
        }



    }
    

    public int top() {
    // handle empty case before peek which throws EmptyStackException

        if(this.stack.empty()) return 0;
        return this.stack.peek();
    }
    
    public int getMin() {
        if(this.minStack.empty()) return 0;
        return this.minStack.peek();
    }
}
