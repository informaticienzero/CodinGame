import System.IO
import Control.Monad

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    
    -- Auto-generated code below aims at helping you parse
    -- the standard input according to the problem statement.
    
    input_line <- getLine
    let n = read input_line :: Int
    
    -- hPutStrLn stderr "Debug messages..."
    
    -- Write answer to stdout
    putStrLn (show (n * n - sum [n `mod` d | d <- [1..n]]))
    return ()