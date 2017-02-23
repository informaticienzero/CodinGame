using System;

class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');
        int A = int.Parse(inputs[0]);
        int B = int.Parse(inputs[1]);

        string output = string.Empty;

        char d1 = A.ToString()[0];
        char d2 = B.ToString()[0];

        int toPrint = 0;

        output += new string(d1, A);
        toPrint += A;

        if (output.Length > 1)
        {
            output += new string(d2, A);
            toPrint += A;
        }
        else
        {
            output += new string(d2, B);
            toPrint += B;
        }

        // Main loop.
        for (int n = 2; toPrint < N; ++n)
        {
            int digit = (int) char.GetNumericValue(output[n]);
            char digitToPrint = char.MinValue;

            if (n % 2 == 0)
            {
                digitToPrint = d1;
            }
            else
            {
                digitToPrint = d2;
            }

            output += new string(digitToPrint, digit);
            toPrint += digit;
        }
        
        output = output.Substring(0, N);
        Console.WriteLine(output);
    }
}
