package com.example.demo.models;

public class Product {
    Integer id;
    String name;
    Brand brand;
    Integer stock;

    public Product(Integer id, String name, Brand brand, Integer stock, Product parent) {
        this.id = id;
        this.name = name;
        this.brand = brand;
        this.stock = stock;
        this.parent = parent;
    }

    Product parent;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Brand getBrand() {
        return brand;
    }

    public void setBrand(Brand brand) {
        this.brand = brand;
    }

    public Integer getStock() {
        return stock;
    }

    public void setStock(Integer stock) {
        this.stock = stock;
    }

    public Product getParent() {
        return parent;
    }

    public void setParent(Product parent) {
        this.parent = parent;
    }
}
