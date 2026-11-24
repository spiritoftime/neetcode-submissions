class MinStack {
    constructor() {
        this.stack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        const min = this.stack.length === 0 ? 
        val : 
        Math.min(val, this.stack[this.stack.length - 1][1]);
        this.stack.push([val, min]);
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.stack.length === 0) return null;
        return this.stack.pop()[0];
    }

    /**
     * @return {number}
     */
    top() {
        if (this.stack.length === 0) return null;
        return this.stack[this.stack.length - 1][0];
    }

    /**
     * @return {number}
     */
    getMin() {
        if (this.stack.length === 0) return null;
        return this.stack[this.stack.length - 1][1];
    }
}
