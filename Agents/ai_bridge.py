from pydantic import BaseModel,EmailStr,PositiveInt,ValidationError



class GemniResponse(BaseModel):
    text:str
    tokens:PositiveInt
    success:str
    email:EmailStr

try:
    response1 = GemniResponse(
        text="Python is a programing lanuage",
        tokens = 100,
        success="true",
        email="hiren@gmail.com@Yahoo.com"
    )

    print(response1)
except ValidationError as e:
    print("Error:",e)
