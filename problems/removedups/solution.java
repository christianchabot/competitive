import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.System;
import java.lang.StringBuilder;

public class solution {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		try {
			input = br.readLine();
		} catch(Exception e) {
			return;
		}
		StringBuilder output = new StringBuilder();

		for (char c : input.toCharArray())
			if (output.toString().indexOf(c) == -1)
				output.append(c);

		System.out.println(output.toString());
	}
}
