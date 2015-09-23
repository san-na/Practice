factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

bmiCalc :: Double -> Double -> String
bmiCalc weight height
    | bmi <= skinny = "underweight"
    | bmi <= normal = "normal"
    | bmi <= fat    = "fat"
    | otherwise     = "null"
    where bmi = weight / height ^ 2
          skinny = 18.5
          normal = 25.0
          fat = 30.0


