package com.example.demo.controllers;

import com.example.demo.models.Product;
import com.example.demo.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class ProductController {
    @Autowired
    ProductRepository productRepository;

    @GetMapping("/products")
    public Map<String, List<Product>> getAllProducts() {
        return new HashMap<>() {{ put("products", productRepository.getAllProducts()); }};
    }

    @GetMapping("/products/{id}")
    public Map<String, Product> getProductById(@PathVariable Integer id) {
        return new HashMap<>() {{ put("product", productRepository.getProduct(id)); }};
    }

    @GetMapping("/brands/{id}/products")
    public Map<String, List<Product>> getProductByBrand(@PathVariable Integer id) {
        return new HashMap<>() {{ put("product", productRepository.getProductsByBrand(id)); }};
    }
}
