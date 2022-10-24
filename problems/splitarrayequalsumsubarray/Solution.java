import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.lang.Integer;
import java.lang.String;
import java.lang.System;

import java.util.ArrayList;

public class Solution {
	public static void main(String args[]) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] nums;

		try {
			nums = br.readLine().split(" ");
		} catch (Exception e) {
			return;
		}

		int l = 0, r = nums.length - 1;
		int lsum = Integer.parseInt(nums[l]), rsum = Integer.parseInt(nums[r]);
		while (l < r) {
			if (lsum == rsum && l + 2 == r) {
				System.out.println(l + 1);
				return;
			} else if (lsum < rsum)
				lsum += Integer.parseInt(nums[++l]);
			else
				rsum += Integer.parseInt(nums[--r]);
		}
	}
}
