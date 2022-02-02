package com.example.demo.repositories;

import com.example.demo.models.Brand;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class BrandRepository {
    List<Brand> BRANDS = new ArrayList<>(
            Arrays.asList(
                    new Brand(1, "Apple"),
                    new Brand(2, "Huawei"),
                    new Brand(3, "Dell")
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
}
