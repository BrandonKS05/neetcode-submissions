/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if (head == null) return;

        List<ListNode> newlist = new ArrayList<>();
        ListNode cur = head;
        while (cur != null) {
            newlist.add(cur);
            cur = cur.next;
        }

        int l = 0;
        int r = newlist.size() - 1;
        while (l < r - 1) {
            newlist.get(l).next = newlist.get(r);
            l++;
            newlist.get(r).next = newlist.get(l);
            r--;
            newlist.get(l).next = newlist.get(r);
        }
        newlist.get(r).next = null;
    }
}
