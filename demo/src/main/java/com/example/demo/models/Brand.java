package com.example.demo.models;

public class Brand {
    Integer id;
    String name;
    String description;
    String hq;

    public Brand(Integer id, String name, String description, String hq) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.hq = hq;
    }

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

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getHq() {
        return hq;
    }

    public void setHq(String hq) {
        this.hq = hq;
    }
}
