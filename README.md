# Gym-Tracker

Web app to track weight and repetitions for exercises in the gym

> exercises schema

```
{
    "name": str,
    "uid": str,
}
```

> user schema

```
{
    "username" : str,
    "uid" : str
}
```

> workout schema

```
{
    "exercise": str
    "sets": [{
        "weight": int,
        "reps": int
    }]
}
```
