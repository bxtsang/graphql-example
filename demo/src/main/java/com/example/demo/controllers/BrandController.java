package com.example.demo.controllers;

import com.example.demo.models.Brand;
import com.example.demo.repositories.BrandRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class BrandController {

    @Autowired
    BrandRepository brandRepository;

    @GetMapping("/brands")
    public Map<String, List<Brand>> getAllBrands() {
        return new HashMap<>() {{ put("brands", brandRepository.getAllBrands()); }};
    }

    @GetMapping("/brands/{id}")
    public Map<String, Brand> getBrandById(@PathVariable Integer id) {
        return new HashMap<>() {{ put("brands", brandRepository.getBrand(id)); }};
    }

    @PostMapping("/brands")
    public Map<String, Brand> addBrand(Map<String, String> brandInput) {
        return new HashMap<>() {{ put("brands", brandRepository.addBrand(brandInput)); }};
    }
 }
