package com.example.demo.repositories;

import com.example.demo.models.Brand;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

@Service
public class BrandRepository {
    List<Brand> BRANDS = new ArrayList<>(
            Arrays.asList(
                    new Brand(1, "Apple", "I keep the doctor away if you eat one of me a day", "California"),
                    new Brand(2, "Huawei", "Chinese company with pretty good phones but no Android", "Shenzhen"),
                    new Brand(3, "Dell", "I make pretty good laptops", "Texas")
            )
    );

    public List<Brand> getAllBrands() {
        return BRANDS;
    }

    public Brand getBrand(Integer id) {
        for (Brand brand: BRANDS) {
            if (brand.getId() == id) {
                return brand;
            }
        }
        throw new ResponseStatusException(HttpStatus.NOT_FOUND);
    }

    public Brand addBrand(Map<String, String> brandInput) {
        Brand newBrand = new Brand(BRANDS.size() + 1, brandInput.get("name"), brandInput.get("description"), brandInput.get("hq"));
        BRANDS.add(newBrand);

        return newBrand;
    }
}
