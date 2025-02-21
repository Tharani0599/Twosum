from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

def two_sum(num, t):
    d = {}
    for i, value in enumerate(num):
        if (t - value) in d:
            return [d[t - value], i]
        else:
            d[value] = i
    return []  

class TwoSumRequest(BaseModel):
    num: list[int]
    t: int

@app.post("/two-sum")
def find_two_sum(request: TwoSumRequest):
    result = two_sum(request.num, request.t)
    if result:
        return {"indices": result}
    else:
        raise HTTPException(status_code=404, detail="bye")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)