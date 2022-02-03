package com.example.demo.controllers;

import com.example.demo.models.Brand;
import com.example.demo.repositories.BrandRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
public class BrandController {

    @Autowired
    BrandRepository brandRepository;

    @GetMapping("/brands")
    public List<Brand> getAllBrands() {
        return brandRepository.getAllBrands();
    }

    @GetMapping("/brands/{id}")
    public Brand getBrandById(@PathVariable Integer id) {
        return brandRepository.getBrand(id);
    }

    @PostMapping("/brand")
    public Brand addBrand(Map<String, String> brandInput) {
        return brandRepository.addBrand(brandInput);
    }
}
