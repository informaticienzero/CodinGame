using System;

class Player
{
    // Used only because C# tuples are immutables.
    class Point
    {
        public int X { get; set; }
        public int Y { get; set; }
    }
    
    static void Main(string[] args)
    {
        #region Init
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]); // width of the building.
        int H = int.Parse(inputs[1]); // height of the building.
        int N = int.Parse(Console.ReadLine()); // maximum number of turns before game over.
        inputs = Console.ReadLine().Split(' ');
        int X0 = int.Parse(inputs[0]);
        int Y0 = int.Parse(inputs[1]);
        #endregion
        
        // Zone to look in.
        var limits = new Point[2]
        {
            new Point { X = 0, Y = 0 },
            new Point { X = W, Y = H }
        };
        
        while (true)
        {
            string bombDirection = Console.ReadLine();
            
            Console.Error.WriteLine(string.Format("Batman position ({0};{1})", X0, Y0));
            Console.Error.WriteLine(string.Format("Bomb direction == {0}", bombDirection));
            
            if (bombDirection.Contains("U"))
            {
                limits[1].Y = Y0;
            }
            if (bombDirection.Contains("D"))
            {
                limits[0].Y = Y0;
            }

            if (bombDirection.Contains("R"))
            {
                limits[0].X = X0;
            }
            if (bombDirection.Contains("L"))
            {
                limits[1].X = X0;
            }

            X0 = (limits[0].X + limits[1].X) / 2;
            Y0 = (limits[0].Y + limits[1].Y) / 2;
            
            Console.WriteLine(string.Format("{0} {1}", X0, Y0));
        }
    }
}
