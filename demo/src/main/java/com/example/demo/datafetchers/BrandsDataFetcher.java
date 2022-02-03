package com.example.demo.datafetchers;

import com.example.demo.models.Brand;
import com.example.demo.models.Product;
import com.example.demo.repositories.BrandRepository;
import com.example.demo.repositories.ProductRepository;
import com.netflix.graphql.dgs.DgsComponent;
import com.netflix.graphql.dgs.DgsData;
import com.netflix.graphql.dgs.DgsDataFetchingEnvironment;
import com.netflix.graphql.dgs.DgsQuery;
import com.netflix.graphql.dgs.exceptions.DgsInvalidInputArgumentException;
import graphql.schema.DataFetchingEnvironment;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@DgsComponent
public class BrandsDataFetcher {
    @Autowired
    BrandRepository brandRepository;

    @Autowired
    ProductRepository productRepository;

    @DgsQuery
    public List<Brand> brands() {
        return brandRepository.getAllBrands();
    }

    @DgsData(parentType = "Brand", field = "products")
    public List<Product> products(DgsDataFetchingEnvironment dfe) {
        Brand brand = dfe.getSource();
        return productRepository.getProductsByBrand(brand.getId());
    }

    @DgsData(parentType = "Mutation", field = "addBrand")
    public Brand addBrand(DataFetchingEnvironment dataFetchingEnvironment) {
        if (! dataFetchingEnvironment.containsArgument("name") || ! dataFetchingEnvironment.containsArgument("description") || ! dataFetchingEnvironment.containsArgument("hq")) {
            throw new DgsInvalidInputArgumentException("Missing Arguments", null);
        }

        String name = dataFetchingEnvironment.getArgument("name");
        String description = dataFetchingEnvironment.getArgument("description");
        String hq = dataFetchingEnvironment.getArgument("hq");

        Map<String, String> brandInput = new HashMap<>();
        brandInput.put("name", name);
        brandInput.put("description", description);
        brandInput.put("hq", hq);

        return brandRepository.addBrand(brandInput);
    }
}
