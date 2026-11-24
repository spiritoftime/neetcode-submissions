class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const res = new Array(temperatures.length).fill(0);
        const st = []; // Stack to hold [temperature, index]

        for (let i = 0; i < temperatures.length; i++) {
            const currTemp = temperatures[i];

            while (st.length > 0 && currTemp > st[st.length - 1][0]) {
                const [prevTemp, prevIndex] = st.pop();
                res[prevIndex] = i - prevIndex;
            }

            st.push([currTemp, i]);
        }

        return res;
    }
}
