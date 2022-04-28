export interface Product{
    id: number,
    name: string;
    description: string;
    price: number;
    filename: string;
    height: number;
    width: number;
    rating: number;
    count:number;
}

export interface Category{
    id: number;
    name: string;
}

export interface Shop{
    id: number;
    name: string;
    description: string;
}

export interface City{
    id: number;
    name: string;
}

export interface AuthToken {
    token: string;
}
