class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hm = {}

        for(let s of strs){
            const sortedS = s.split('').sort().join('');
            if(sortedS in hm){
                hm[sortedS].push(s)
            }
            else{
                hm[sortedS] = [s]
            }
        }

        return  Object.values(hm)
    }
}
